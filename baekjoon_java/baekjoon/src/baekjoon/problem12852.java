package baekjoon;

import java.util.Scanner;

public class problem12852 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int dp[] = new int[N+1];
		int temp[] = new int[N+1];
				
		dp[1] = 0;
		
		for(int i=2; i<N+1; i++) {
			dp[i] = dp[i-1]+1;
			temp[i] = i-1;
			
			if(i%3==0 && dp[i]> dp[i/3]+1) {
				dp[i] = dp[i/3]+1;
				temp[i] = i/3;
			}
			
			if(i%2==0 && dp[i]> dp[i/2]+1) {
				dp[i] = dp[i/2]+1;
				temp[i] = i/2;
			}
			
		}
		
		System.out.println(dp[N]);
		while(N > 0) {
			System.out.print(N+" ");
			N = temp[N];
		}
	}

}
