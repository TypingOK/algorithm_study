package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;
public class problem10826 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		if(n>=2) {
		BigInteger[] dp = new BigInteger[n+1];
		dp[0]=BigInteger.ZERO;
		dp[1]=BigInteger.ONE;
		
			for(int i=2; i<n+1; i++) {
				dp[i]=dp[i-1].add(dp[i-2]);
			}
			System.out.println(dp[n]);
		}
		else if (n==1) {
			System.out.println(1);
		}
		else if (n==0) {
			System.out.println(0);
		}
		
	}

}
