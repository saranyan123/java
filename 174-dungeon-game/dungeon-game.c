#include <stdio.h>
#include <math.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int calculateMinimumHP(int** dungeon, int dungeonSize, int* dungeonColSize) {
    int m = dungeonSize;
    int n = dungeonColSize[0];
    
    // Use a 2D array for DP
    int dp[m][n];

    // Base case: Princess room
    dp[m-1][n-1] = MAX(1, 1 - dungeon[m-1][n-1]);

    // Fill last column
    for (int i = m - 2; i >= 0; i--) {
        dp[i][n-1] = MAX(1, dp[i+1][n-1] - dungeon[i][n-1]);
    }

    // Fill last row
    for (int j = n - 2; j >= 0; j--) {
        dp[m-1][j] = MAX(1, dp[m-1][j+1] - dungeon[m-1][j]);
    }

    // Fill remaining cells
    for (int i = m - 2; i >= 0; i--) {
        for (int j = n - 2; j >= 0; j--) {
            int min_next = MIN(dp[i+1][j], dp[i][j+1]);
            dp[i][j] = MAX(1, min_next - dungeon[i][j]);
        }
    }

    return dp[0][0];
}
