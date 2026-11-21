from math import comb, log
# ---- observed data (Emily's own counts) ----
OKC_SEEN=1200; OKC_LIKE=9; OKC_CONV=2
HIN_MATCH=4; HIN_CONV=2
CONV=OKC_CONV+HIN_CONV          # 4
MEET=1

def wilson(k,n,z=1.96):
    if n==0: return (0,1)
    p=k/n; d=1+z*z/n
    c=(p+z*z/(2*n))/d
    h=z*((p*(1-p)/n+z*z/(4*n*n))**0.5)/d
    return (max(0,c-h),min(1,c+h))

def jeff(k,n):
    # Jeffreys interval via beta quantiles, crude numeric
    from statistics import NormalDist
    try:
        from scipy.stats import beta
        return beta.ppf(0.025,k+0.5,n-k+0.5), beta.ppf(0.975,k+0.5,n-k+0.5)
    except Exception:
        return None

print("=== OBSERVED ===")
print(f" OkCupid like rate      {OKC_LIKE}/{OKC_SEEN} = {OKC_LIKE/OKC_SEEN*100:.2f}%  (1 in {OKC_SEEN/OKC_LIKE:.0f})")
lo,hi=wilson(OKC_LIKE,OKC_SEEN); print(f"   95% CI {lo*100:.2f}% - {hi*100:.2f}%")
print(f" like -> conversation   {OKC_CONV}/{OKC_LIKE} = {OKC_CONV/OKC_LIKE*100:.0f}%")
print(f" seen -> conversation   {OKC_CONV}/{OKC_SEEN} = 1 in {OKC_SEEN/OKC_CONV:.0f}")
print(f" Hinge match -> conv    {HIN_CONV}/{HIN_MATCH} = {HIN_CONV/HIN_MATCH*100:.0f}%")
print(f" conversation -> meet   {MEET}/{CONV} = {MEET/CONV*100:.0f}%")
lo,hi=wilson(MEET,CONV); print(f"   95% CI {lo*100:.0f}% - {hi*100:.0f}%   <- n=4, estimate is near-worthless")
j=jeff(MEET,CONV)
if j: print(f"   Jeffreys 95% CI {j[0]*100:.0f}% - {j[1]*100:.0f}%")

print("\n=== P(zero meetings) at various true per-conversation rates ===")
print(" n conv |" + "".join(f"  p={p:.2f}" for p in (0.10,0.15,0.20,0.25,0.30)))
for n in (4,6,10,15,20,30):
    row=f"   {n:3d}  |"
    for p in (0.10,0.15,0.20,0.25,0.30):
        row+=f"   {(1-p)**n*100:5.1f}%"
    print(row)

print("\n=== PROFILES NEEDED (at observed rates, p_meet=0.25) ===")
seen_per_conv=OKC_SEEN/OKC_CONV
for target in (1,3,5):
    convs=target/0.25
    print(f"  {target} meeting(s): {convs:.0f} conversations = {convs*seen_per_conv:,.0f} profiles seen")

print("\n=== THROUGHPUT at 200 profiles/week ===")
wk=200
cpw=wk/seen_per_conv
print(f"  conversations/week {cpw:.2f}   /year {cpw*52:.1f}")
print(f"  meetings/year      {cpw*52*0.25:.1f}")
print(f"  weeks per meeting  {1/(cpw*0.25):.0f}  = {1/(cpw*0.25)/52:.1f} years")

print("\n=== TIME TO FIRST MEETING, 50/90% ===")
import math
p_week=cpw*0.25   # expected meetings per week
for q in (0.5,0.9):
    # P(>=1 meeting in w weeks) with Poisson rate p_week
    w=-math.log(1-q)/p_week
    print(f"  {int(q*100)}% chance of >=1 meeting after {w:.0f} weeks = {w/52:.1f} years")
