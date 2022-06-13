package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 지금 수가 비교하는 수보다 크면 1 작으면 -1

public class problem17178 {

	static class Test implements Comparable<Test>{
		char c;
		int num;
		
		public Test(char c, int num) {
			this.c = c;
			this.num = num;
		}
		
		@Override
		public int compareTo(Test o) {
			if((this.c -o.c)<0 ) {
				return -1;
			}else if(this.c - o.c ==0) {
				if((this.num - o.num)<0) {
					return -1;
				}else {
					return 1;
				}
			}else {
				return 1;
			}
		}
		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		ArrayList<Test> wating = new ArrayList<>();
		ArrayList<Test> st = new ArrayList<>();

		String str[];

		for (int i = 0; i < N; i++) {
			str = br.readLine().split(" ");
			for (int j = 0; j < 5; j++) {
				String[] temp = str[j].split("-");
				wating.add(new Test(temp[0].charAt(0),Integer.parseInt(temp[1])));
			}

		}
		
		
		int size = wating.size();
		while (size != 0) {
			int stackSize = st.size(); //스택에 있는 사람 중에 나갈 수 있는지 확인
			if (stackSize != 0) {
				boolean flag = false;
				Test peek = st.get(stackSize - 1);
				for(int i=0; i<size; i++) {
					if(peek.compareTo(wating.get(i))>=1) {
						flag = true;
						break;
					}
				}
				if(!flag) {
					st.remove(stackSize-1);
					continue;
				}
			}
			
			
			Test now = wating.get(0);
			wating.remove(0);
			size-=1;
			
			
			for(int i=0; i<size; i++) {
				if(now.compareTo(wating.get(i)) >= 1) {
					for(int j=0; j<stackSize; j++) {
						if(now.compareTo(st.get(j))>=1) {
							System.out.println("BAD");
							System.exit(0);
						}
					}
					st.add(now);
					break ;
				}
			}
		}
		System.out.println("GOOD");
	}

}
