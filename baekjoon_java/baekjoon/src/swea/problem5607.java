package swea;

import java.io.BufferedReader;
import java.util.Scanner;

public class problem5607 {
	static final int P = 1234567891;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for(int tc=1; tc<=TC; tc++) {
			int N = sc.nextInt();
			int R = sc.nextInt();
			
			long numer = factorial(N);
			long denom = factorial(R) * factorial(N-R) %P;
			
			System.out.println("#"+tc+" "+(numer * pow (denom, P-2) % P));
		}
	}
	
	static long factorial(int N) {
		long fac = 1L;
		
		while(N>1) {
			fac = (fac * N) % P;
			N--;
		}
		
		return fac;
	}
	
	static long pow(long base, long e) {
		if(e == 1) {
			return base % P;
		}
		
		long temp = pow(base, e/2);
		
		if(e % 2==1) {
			return (temp*temp % P) * base%P;
		}
		return temp*temp%P;
	}

}
