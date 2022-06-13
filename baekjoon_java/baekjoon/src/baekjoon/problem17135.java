package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class problem17135 {
	static int[][] origin,copy;
	static int N,M,D;
	static int ans;
	static boolean[] archers;
	
	static int[] di = {0,-1,0}; //위
	static int[] dj = {-1,0,1}; //왼쪽, 오른쪽
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		D = sc.nextInt();
		
		origin = new int[N][M];
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				origin[i][j] = sc.nextInt();
			}
		} // end input
		
		archers = new boolean[M];
		comb(0,0);
		System.out.println(ans);
	}
	
	static void comb(int idx,int cnt) {
		if(cnt == 3) { // 궁수 3명 배치됨!
			
			
			copy = new int[N+1][M];
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					copy[i][j] = origin[i][j];
				}
			}
			
//			System.out.println(Arrays.toString(archers));
			int tmp = 0;
			for(int i=0; i<N; i++) {
				tmp += bfs(copy);
				move(copy);
			}
			
			ans = Math.max(ans, tmp);
			return;
		}
		
		if(idx == M) {
			return ;
		}
		
		archers[idx] = true;
		comb(idx+1, cnt+1);
		archers[idx] = false;
		comb(idx+1,cnt);
	}
	
	static void print(int[][] map) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(map[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	private static void move(int[][] map) {
		for(int i=N-1; i>0; i--) {
			for(int j=0; j<M; j++) {
				map[i][j] = map[i-1][j];
			}
		}
		for(int j=0; j<M; j++) { // 한줄 내려갔으니까 맨 위에 비워주기
			map[0][j] = 0;
		}
	}
	
	private static int bfs(int[][] map) {
		boolean[][] shoot = new boolean[N][M];
		
		for(int j=0; j<M; j++) {
			
			if(archers[j]) { // 궁수 위치하는 j칸 찾아서 큐에 집어넣기
				Queue<Point> queue = new LinkedList<>();
				PriorityQueue<Point> enemy = new PriorityQueue<>(); // 적의 좌표만 넣기
				boolean[][] visit = new boolean[N][M];
				
				queue.add(new Point(N, j));
				
				int dist = 0;
				while(!queue.isEmpty() && dist <= D) {// 현재 큐에 들어있는 좌표까지의 거리가 D 이하인 경우에만 진행
					int size = queue.size();
					
					for(int s=0; s<size; s++) {
						Point now = queue.poll();

						if(map[now.i][now.j]==1) {
							enemy.add(now);
						}
						for(int d=0; d<3; d++) {
							int ni = now.i+ di[d];
							int nj = now.j+ dj[d];
							
							if(ni>=0 && ni<N && nj>=0 && nj<M && !visit[ni][nj]) {
								queue.add(new Point(ni, nj));
								visit[ni][nj] = true;
							}
						}
					}
					dist++;
					if(!enemy.isEmpty()) { //현재 궁수가 쏠 적을 찾았을 때 저장
						Point target = enemy.poll();
						shoot[target.i][target.j] = true;
						break; //이번 궁수는 타깃 정했으니 다음 궁수 ㄱㄱ
					}
				}
				
			}
		} // 모든 궁수가 타겟을 찾은 경우
		int cnt = 0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(shoot[i][j]) {
					map[i][j] = 0;
					cnt++;
				}
			}
		}
		return cnt;
	}
	
	static class Point implements Comparable<Point>{
		int i,j;
		Point(int i, int j ){
			this.i = i;
			this.j = j;
		}
		
		@Override
		public int compareTo(Point o) {
			return this.j - o.j;
		}
	}
}
