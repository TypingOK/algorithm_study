package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1292 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		int[] a = new int[1002];
		int cnt = 0;
		for(int i=1; i<=m; i++) {
			for(int j=0; j<i; j++) {
				if(cnt==1001) {
					break;
				}
				a[cnt]=i;
				cnt++;
			}
		}
		int sum=0;
		for(int i=n-1; i<m; i++) {
			sum+=a[i];
		}
		System.out.println(sum);
	}

}
