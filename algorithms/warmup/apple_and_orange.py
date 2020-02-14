def count_apples_and_oranges(s, t, a, b, apples, oranges):
    aLanding = [apple + a for apple in apples if (apple + a ) >= s and (apple + a) <= t]
    oLanding = [orange + b for orange in oranges if (orange + b) >= s and (orange + b) <=t]
    print(f"{len(aLanding)}\n{len(oLanding)}")

    
