package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class problem1181 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		String[] str = new String[a];
		for(int i =0; i<a; i++) {
			str[i]=br.readLine();
		}
		Arrays.sort(str, new Comparator<String>() {

			@Override
			public int compare(String s1, String s2) {
				if(s1.length() == s2.length()) {
					return s1.compareTo(s2);
				}else {
					return s1.length()-s2.length();					
				}
			}
		});
		
		StringBuilder sb = new StringBuilder();
		sb.append(str[0]).append('\n');
		for(int i=1; i<a; i++) {
			if(!str[i].equals(str[i-1])) {
				sb.append(str[i]).append("\n");
			}
		}
		System.out.println(sb);
	}

}
