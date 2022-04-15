import java.util.*;

public class Solution {
    static int canJump(int idx, int[] arr, int[] dp) {
        if (idx == 0) {
            return 0;
        }
        if (dp[idx] != -1) {
            return dp[idx];
        }
        int left = canJump(idx - 1, arr, dp) + Math.abs(arr[idx - 1] - arr[idx]);
        int right = Integer.MAX_VALUE;
        if (idx > 1) {
            right = canJump(idx - 2, arr, dp) + Math.abs(arr[idx - 2] - arr[idx]);
        }
        dp[idx] = Math.min(left, right);
        return dp[idx];
    }

    public static int frogJump(int n, int heights[]) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return canJump(n - 1, heights, dp);

    }

}