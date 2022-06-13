package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2003 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		String[] st = br.readLine().split(" ");
		int[] num= new int[n];
		for(int i=0; i<n; i++) {
			num[i]=Integer.parseInt(st[i]);
		}
		int start=0;
		int end=0;
		int sum=0;
		int count=0;
		while(true) {
			if(sum>=m) {
				sum-=num[start++];
				
			}else if(end>=n) {
				break;
			}
			
			else {
				sum+=num[end++];
			}
			if(sum==m) {
				count++;
			}
		}
		System.out.println(count);
	}
}
