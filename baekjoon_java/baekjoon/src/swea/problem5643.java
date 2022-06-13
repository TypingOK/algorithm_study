package swea;

import java.util.Arrays;
import java.util.Scanner;

public class problem5643 {

	static final int max = 987654321; 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for (int tc = 1; tc <= TC; tc++) {

			int N = sc.nextInt();
			int M = sc.nextInt();

			int student[][] = new int[N + 1][N + 1];

			for (int i = 0; i < M; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				student[a][b] = 1;
			}

			for (int k = 1; k <= N; k++) {
				for (int i = 1; i <= N; i++) {
					for (int j = 1; j <= N; j++) {
						if (student[i][k] == 1 && student[k][j] == 1) {
							student[i][j] = 1;
						}
					}
				}
			}
			int ans[] = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
//					System.out.print(student[i][j]+" ");
					if (student[i][j] != 0) {
						ans[i]++;
						ans[j]++;
					}
				}
//				System.out.println();
			}
			int answer = 0;
			for (int i = 1; i <= N; i++) {
				System.out.println(ans[i]);
				if (ans[i] == N - 1) {
					answer++;
				}
			}
//			System.out.println("-----------------------"+answer);
			System.out.println("#"+tc+" "+answer);
		}
	}

}
