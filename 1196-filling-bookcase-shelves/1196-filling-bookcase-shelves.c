int minHeightShelves(int** books, int booksSize, int* booksColSize, int shelfWidth) {
    // dp 사용하는 문제
    // dp array 초기화
    // dp는 책장을 쌓는데 필요한 최소 높이 저장
    // int 포인터 dp가 int 타입의 데이터 가리킴
    // (int*) : 타입 캐스팅 연산자; malloc은 void*타입의 포인터를 반환하므로 이를 int* 타입으로 변환,  포인트 타입 일치하도록
    // malloc 동적 메모리 할당 함수, booksSize + 1 크기만큼 배열 만듬,  그 시작 주소를 반환
    // int 타입 사이즈(4바이트)
    // booksSize +1 개의 int 타입 변수를 저장할 수 있는 메모리 공간 할당.
    int* dp = (int*)malloc((booksSize + 1) * sizeof(int));
    // 책이 없는 경우 높이 0
    dp[0] = 0;
    // 책 배열을 순회
    // 외부 루프 (책 배열 순회)
    for (int i = 1; i <= booksSize; ++i) {
        int w = books[i - 1][0];
        int h = books[i - 1][1];
        // 이전 책까지의 높이에 현재 책 높이를 더한 값
        dp[i] = dp[i - 1] + h;
        // 이전 책들 확인하면서 현태 책 포함하는 경우
        for (int j = i - 1; j > 0; --j) {
            // w에 이전 책 너비 더함
            w += books[j-1][0];
            // w가 최대 너비 초과하면 더 이상 책을 추가할 수 없으므로, 내부 루프 종료
            if (w > shelfWidth) {
                break;
            }
            // h 업데이트
            h = (h > books[j-1][1]) ? h : books[j-1][1];
            // dp에 현재 계산된 높이 와 이전 책들로 계산된 높이 중 최소값으로 업데이트
            dp[i] = (dp[i] < dp[j - 1] + h) ? dp[i] : dp[j-1] + h;
        }
    }
    // 모든 책을 쌓았을 때의 최소 높이 저장
    int result = dp[booksSize];
    // 메모리 해제
    free(dp);
    return result;
}