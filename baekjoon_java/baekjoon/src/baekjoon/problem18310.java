package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class problem18310 {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String str[] = br.readLine().split(" ");
		int[]a = new int[N];
		for(int i=0; i<N; i++) {
			a[i]=Integer.parseInt(str[i]);
		}
		Arrays.sort(a);
		if(N%2==0) {
			System.out.println(a[N/2-1]);			
		}
		else {
			
			System.out.println(a[N/2]);			
		}
	}

}
