def largestPermutation(k, arr):
        n = len(arr)
        h = {x:i for i,x in enumerate(arr)}

        i = 0
        while n > 0 and k > 0:
            if arr[i] < n:
                x = h[n]
                #swap in the array
                arr[h[n]], arr[i] = arr[i], n
                y = h[arr[h[n]]]
                # change the values in hashmap
                h[arr[h[n]]], h[n] = h[n], y
                k -= 1
            n -= 1
            i += 1
        # return arr

if __name__ == "__main__":
    largestPermutation(2, [3,4,2,5,1])
