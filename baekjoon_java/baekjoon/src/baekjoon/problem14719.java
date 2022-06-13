package baekjoon;

import java.util.Scanner;
import java.util.Stack;

public class problem14719 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int H = sc.nextInt();
		int N = sc.nextInt();
		int map[] = new int[N];
		for(int i=0; i<N; i++) {
			map[i] = sc.nextInt();
		}
		Stack<Integer> st = new Stack<>();
		
		int answer=0;
		
		for(int i=0; i<N; i++) {
			//직전보다 값이 크다면
			System.out.println(st);
			while(!st.isEmpty() && map[i]>map[st.peek()]) {
				int top = st.pop();
				
				if(st.size()==0) {
					break;
				}
				System.out.println("i --------------------"+ i);
				System.out.println(top);
				System.out.println(st.peek());
				//이전과의 차이만큼 계산하기
				int dist = i-st.peek()-1;
				System.out.print("dist "+ dist+ " ");
				int water = Math.min(map[i],map[st.peek()]) - map[top];
				System.out.println("water "+water);
				answer+=(dist*water);
			}
			System.out.println();
			st.add(i);
		}
		
		System.out.println(answer);
	}

}
