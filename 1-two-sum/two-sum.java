import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> prevMap = new HashMap<>();



    for (int i = 0; i < nums.length; i++) {
        int diff = target - nums[i];

        if (prevMap.containsKey(diff)) {
            return new int[] { prevMap.get(diff), i };
        }
        prevMap.put(nums[i], i);
    }
    return new int[] {};
}

    public static void main(String[] args) {
        Solution sol = new Solution();
        

        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = sol.twoSum(nums, target);
        
        System.out.println("Indices: " + Arrays.toString(result));
    }
}
