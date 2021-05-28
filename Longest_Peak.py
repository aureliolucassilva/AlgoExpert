def longestPeak(array):
    field = len(array)
    peaks = []
    # Field
    for idx in range(1, field - 1):
        if array[idx - 1] < array[idx] and array[idx + 1] < array[idx]:
            left = idx - 2
            right = idx + 2
            lenght = 3
            # Left
            if left >= 0:
                while array[left] < array[left + 1]:
                    lenght += 1
                    left -= 1
                    if left >= 0:
                        break
            # Right
            if right <= field - 1:
                while array[right] < array[right - 1]:
                    lenght += 1
                    right += 1
                    if right >= field - 1:
                        break
            peaks.append(lenght)
    if len(peaks):
        return max(peaks)
    else:
        return []
