def classPhotos(redShirtHeights, blueShirtHeights):
    # Sort arrays
    redShirtHeights = sorted(redShirtHeights)
    blueShirtHeights = sorted(blueShirtHeights)

    # Photo
    if redShirtHeights[0] > blueShirtHeights[0]:
        photo = list(zip(redShirtHeights, blueShirtHeights))
    else:
        photo = list(zip(blueShirtHeights, redShirtHeights))

    # Follow guidelines?
    guidelines = list(map(lambda x: x[0] > x[1], photo))

    if False in guidelines:
        return False
    else:
        return True
