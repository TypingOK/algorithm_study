package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1149 {
	public static void main(String[] args)  throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int value[][] = new int[N+1][3];
		String[] str;
		for(int i=1; i<N+1; i++) {
			str = br.readLine().split(" ");
			value[i][0]=Integer.parseInt(str[0]);
			value[i][1]=Integer.parseInt(str[1]);
			value[i][2]=Integer.parseInt(str[2]);
		}
		int dp[][] = new int[N+1][3];

		for(int i=1; i<N+1; i++) {
			dp[i][0] = Math.min(dp[i-1][1]+value[i][0], dp[i-1][2]+value[i][0]);
			dp[i][1] = Math.min(dp[i-1][0]+value[i][1], dp[i-1][2]+value[i][1]);
			dp[i][2] = Math.min(dp[i-1][0]+value[i][2], dp[i-1][1]+value[i][2]);
		}
		
		int min = Math.min(dp[N][0], dp[N][1]);
		min = Math.min(min, dp[N][2]);
		System.out.println(min);
	}
}
