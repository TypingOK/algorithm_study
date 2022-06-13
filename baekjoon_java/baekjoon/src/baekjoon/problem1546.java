package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problem1546 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		int[] b = new int[a];
		String[] str = br.readLine().split(" ");
		for(int i=0; i<a; i++) {
			b[i]=Integer.parseInt(str[i]);
		}
		double sum = 0;
		Arrays.sort(b);
		
		for(int i=0; i<b.length; i++) {
			sum += (((double)b[i] / b[b.length - 1]) * 100);
		}
		System.out.print(sum/b.length);
	}
}
