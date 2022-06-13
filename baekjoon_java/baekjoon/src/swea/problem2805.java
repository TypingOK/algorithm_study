package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2805 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=TC; tc++) {
			int n =Integer.parseInt(br.readLine());
			int[][] a = new int[n][n];
			
			for(int i=0; i<n; i++) {
				char[] c = br.readLine().toCharArray();
				for(int j=0; j<n; j++) {
					a[i][j]=c[j]-'0';
				}
			}
			int sum=0;
			for(int i=0; i<n/2; i++) {
				for(int j=n/2-i; j<=n/2+i; j++) {
					sum+=a[i][j];
				}
			}
			for(int i=n/2; i>=0; i--) {
				for(int j=n/2-i; j<=n/2+i; j++) {
					sum+=a[n-i-1][j];
				}
			}
			System.out.println("#"+tc+" "+sum);
		}
	}

}
