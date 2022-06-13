package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2577 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		int c = Integer.parseInt(br.readLine());
		int z = a*b*c;
		String str = String.valueOf(z);
		int[] arr = new int[10];
		for(int i =0; i<str.length(); i++) {
			arr[(int)str.charAt(i)-48]++;
		}
		for(int i=0; i<10; i++) {
			System.out.println(arr[i]);
		}
	}

}
