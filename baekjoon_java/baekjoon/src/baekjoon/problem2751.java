package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problem2751 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		int[] s = new int[T];
		for(int i=0; i<T; i++) {
			s[i]=Integer.parseInt(br.readLine());
		}
		Arrays.sort(s);
		for(int i:s) {
			sb.append(i+"\n");
		}
		System.out.println(sb);
	}
}
