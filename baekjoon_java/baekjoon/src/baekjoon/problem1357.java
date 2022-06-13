package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1357 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str= br.readLine().split(" ");
		StringBuffer st1 = new StringBuffer(str[0]);
		StringBuffer st2 = new StringBuffer(str[1]);
		
		int i = Integer.parseInt(st1.reverse().toString());
		int j = Integer.parseInt(st2.reverse().toString());
		StringBuffer x = new StringBuffer(String.valueOf(i+j));
		int answer = Integer.parseInt(x.reverse().toString());
		System.out.println(answer);
		
	}

}
