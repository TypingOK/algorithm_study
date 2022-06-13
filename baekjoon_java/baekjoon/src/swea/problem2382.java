package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class problem2382 {
	
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int N;
	static int M;
	static int K;
	static ArrayList<Node> n;
	public static class Node implements Comparable<Node>{
		int x;
		int y;
		int m;
		int d;
		Node(int x,int y,int m,int d){
			this.x=x;
			this.y= y;
			this.m=m;
			this.d=d;
		}
		@Override
		public int compareTo(Node o) {
			return o.m-this.m;
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		String str[];
		for(int tc = 1; tc<=TC; tc++) {
			str = br.readLine().split(" ");
			
			N= Integer.parseInt(str[0]); // 배열의 크기
			M = Integer.parseInt(str[1]); // 끝나는 시간
			K = Integer.parseInt(str[2]);  // 미생물의 수
			
			n = new ArrayList<>(K); 
			
			
			for(int i=0; i<K; i++) {
				str = br.readLine().split(" ");
				int x = Integer.parseInt(str[0]);
				int y = Integer.parseInt(str[1]);
				int m = Integer.parseInt(str[2]);
				int d = Integer.parseInt(str[3])-1;
				
				n.add(new Node(x,y,m,d));
			}
			
			
			int size = K;
			for(int i=0; i<M; i++) {
				for(int j=0; j<size; j++) {
					if(moving(n.get(j),j)) {
						i--;
						size--;
					}
				}
				Collections.sort(n);
				for(int j=0; j<size; j++){
					int temp0 = n.get(j).x;
					int temp1 = n.get(j).y;
					for(int k=j+1; k<size; k++) {
						if(temp0==n.get(k).x && temp1==n.get(k).y) {
							n.get(j).m += n.get(k).m;
							n.remove(k);
							size--;
							k--;
						}
					}
				}
			}
			
			int answer = 0;
			for(int i=0; i<size; i++) {
				answer += n.get(i).m;
			}
			System.out.println("#"+tc+" "+answer);
			
		}
	}
	
	static boolean moving(Node l,int index) {
		int x= l.x;
		int y = l.y;
		int m = l.m;
		int d = l.d;
		
		int nx = x+dx[d];
		int ny = y+dy[d];
		if(1<=nx && nx<N-1 && 1<=ny && ny<N-1) {
			n.get(index).x=nx;
			n.get(index).y=ny;
		}else if(0==nx || nx==N-1 || 0==ny || ny==N-1) {
			m = m/2;
			if(m!= 0 ) {
				if(d==0) d=1;
				else if(d==1) d=0;
				else if(d==2) d=3;
				else if(d==3) d=2;
				n.get(index).x=nx;
				n.get(index).y=ny;
				n.get(index).m=m;
				n.get(index).d=d;
			}else if(m<=0) {
				n.remove(index);
				return true;
			}
		}
		return false;
	}
}
