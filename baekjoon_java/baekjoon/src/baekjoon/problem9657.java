package baekjoon;

import java.util.Scanner;

public class problem9657 {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int dp[] = new int[1001]; 
		
		dp[1]=1;
		dp[2] = 0;
		dp[3] = 1;
		dp[4] = 1;
		
		for(int i=5; i<=1000; i++) {
			if(dp[i-1]+dp[i-3]+dp[i-4]<3) {
				dp[i]=1;
			}else {
				dp[i]=0;
			}
		}
		if(dp[N]==1) {
			System.out.println("SK");
		}else {
			System.out.println("CY");
		}
	}

}
