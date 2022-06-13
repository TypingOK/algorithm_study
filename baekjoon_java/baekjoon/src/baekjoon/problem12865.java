package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem12865 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		
		int value[] = new int[N+1];
		int weight[] = new int[N+1];
		int dp[][] = new int[N+1][M+1];
		
		for(int i=1; i<N+1; i++) {
			str = br.readLine().split(" ");
			weight[i] = Integer.parseInt(str[0]);
			value[i] = Integer.parseInt(str[1]);
			
		}
		
		
		for(int i=1; i<N+1; i++) {
			for(int j=1; j<M+1; j++) {
				if(weight[i]>j) {
					dp[i][j] = dp[i-1][j];
				}else {
					dp[i][j] =Math.max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i]);
				}
			}
		}
		System.out.println(dp[N][M]);
	}

}
