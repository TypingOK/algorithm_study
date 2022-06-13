package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class problem1406 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		List<Character> a = new LinkedList<Character>();
		ListIterator<Character> b = a.listIterator();
		
		char[] c = br.readLine().toCharArray();
		for(int i=0; i<c.length; i++) {
			b.add(c[i]);
		}
		
		int N = Integer.parseInt(br.readLine());
		
		String[] str;
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			if(str[0].equals("L")) {
				if(b.hasPrevious()) {
					b.previous();
				}
			}else if(str[0].equals("D")) {
				if(b.hasNext()) {
					b.next();
				}
			}else if(str[0].equals("B")) {
				if(b.hasPrevious()) {
					b.previous();
					b.remove();
				}
			}else if(str[0].equals("P")) {
				b.add(str[1].charAt(0));
			}
		}
		
		for(char z:a) {
			sb.append(z);
		}
		System.out.println(sb.toString());
	}
	
	
}
