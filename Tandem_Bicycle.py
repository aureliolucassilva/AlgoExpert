def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds = sorted(redShirtSpeeds)
    blueShirtSpeeds = sorted(blueShirtSpeeds)

    if fastest:
        pairsFast = list(zip(redShirtSpeeds, reversed(blueShirtSpeeds)))
        maxSpeed = list(map(lambda x: max(x), pairsFast))
        maximum = sum(maxSpeed)
        return maximum
    else:
        pairsSlow = list(zip(redShirtSpeeds, blueShirtSpeeds))
        minSpeed = list(map(lambda x: max(x), pairsSlow))
        minimum = sum(minSpeed)
        return minimum
