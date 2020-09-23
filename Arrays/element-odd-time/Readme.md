## Find that odd

Hackerank URL: https://www.hackerrank.com/contests/codex-2-0-1/challenges/find-that-odd/problem

## Solution

In solution 1 we use a simple mapping trick to get the answer. Even though the time complexity in solution-1 is O(n) but we are taking extra space to make the map.

There is one another way, which is using sorting technique but we should avoid it because:
a) It is bit complex
b) Even if we use heap sort to sort the array the least time complexity would be O(nlogn) without any extra space.

The __optimal__ solution would be to use the XOR operation on this. Just keep on xor-ing all the element with each other. So if the element of the array was `1 2 3 2 1` then the solution would be do 

![](http://www.sciweavers.org/tex2img.php?eq=1%20%5Cbigoplus%202%20%5Cbigoplus%203%20%5Cbigoplus%202%20%5Cbigoplus%201&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

In this method the time complexity would still be `O(n)` but we wouldn't be consuming any extra space.
