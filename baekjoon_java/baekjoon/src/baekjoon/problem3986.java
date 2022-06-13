package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class problem3986 {

	public static void main(String[] args) throws IOException{
		Deque<Character> stack = new ArrayDeque<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int count=0;
		for(int i=0; i<n; i++) {
			char[] c = br.readLine().toCharArray();
			stack.add(c[0]);
			for(int j=1; j<c.length; j++) {
				if(stack.peekLast()!=null && stack.peekLast()==c[j]) {
					stack.removeLast();
				}
				else {
					stack.add(c[j]);
				}
			}
			
			if(stack.isEmpty()) {
				count++;
			}
			else {
				stack.clear();
			}
		}
		System.out.println(count);
	}

}
