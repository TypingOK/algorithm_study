package baekjoon;

import java.io.BufferedReader;
import java.util.Scanner;

public class problem2293 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int[] temp = new int[1001];
		int[] dp = new int[10001];
		for(int i=0; i<n; i++) {
			temp[i] = sc.nextInt();
		}
		dp[0] = 1;
		for (int j = 0; j < n; j++) {
			for (int i = 1; i < k + 1; i++) {
				if(i>=temp[j])
					dp[i] = dp[i]+dp[i-temp[j]];
			}
		}
		System.out.println(dp[k]);
	}

}
