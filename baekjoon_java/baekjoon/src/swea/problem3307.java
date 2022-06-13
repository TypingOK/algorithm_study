package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem3307 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc<=TC; tc++) {
			int N = Integer.parseInt(br.readLine());
			String str[] = br.readLine().split(" ");
			
			int[] a = new int[N+1];
			
			for(int i=1; i<=N; i++) {
				a[i] = Integer.parseInt(str[i-1]);
			}
			
			int [] dp = new int[N+1];
			int max = Integer.MIN_VALUE;
			for(int i=1; i<=N; i++) {
				dp[i] = 1;
				for(int j=1; j<=i-1; j++) {
					if(a[i]>a[j] && 1+dp[j] > dp[i]) {
						dp[i] = 1+dp[j];
					}
				}
				max = Math.max(max, dp[i]);
			}
			System.out.println("#"+tc+" "+max);
		}
	}

}
