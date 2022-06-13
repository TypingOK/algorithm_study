package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problem2230 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		
		int[] a= new int[N];
		for(int i=0; i<N; i++) {
			a[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(a);
		
		
		int min = Integer.MAX_VALUE;
		int start =0;
		int end =1;
		while(end<N) {
			if(a[end]-a[start]>=M) {
				min = Math.min(min, a[end]-a[start]);
				start++;
			}else {
				end++;
			}
			if(start==end) {
				end++;
			}
		}
		System.out.println(min);
	}

}
