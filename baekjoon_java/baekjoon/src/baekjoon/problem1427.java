package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problem1427 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		br.close();
		int[] a = new int[str.length()];
		for(int i =0; i<str.length(); i++) {
			a[i]=(int)str.charAt(i)-'0';
		}
		Arrays.sort(a);
		for(int i = a.length-1; i>=0; i--) {
			System.out.print(a[i]);
		}
	}

}
