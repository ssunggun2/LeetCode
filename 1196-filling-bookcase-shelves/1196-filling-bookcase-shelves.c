int minHeightShelves(int** books, int booksSize, int* booksColSize, int shelfWidth) {
    int* dp = (int*)malloc((booksSize + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i <= booksSize; ++i) {
        int w = books[i - 1][0];
        int h = books[i - 1][1];
        dp[i] = dp[i - 1] + h;
        for (int j = i - 1; j > 0; --j) {
            w += books[j-1][0];
            if (w > shelfWidth) {
                break;
            }
            h = (h > books[j-1][1]) ? h : books[j-1][1];
            dp[i] = (dp[i] < dp[j - 1] + h) ? dp[i] : dp[j-1] + h;
        }
    }
    int result = dp[booksSize];
    free(dp);
    return result;
}