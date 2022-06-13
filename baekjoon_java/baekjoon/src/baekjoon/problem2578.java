package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class problem2578 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] pan = new int[5][5];
		boolean[][] visited = new boolean[5][5];
		for(int i=0; i<5; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0; j<5; j++) {
				pan[i][j] = Integer.parseInt(str[j]);
			}
		}
		int cnt=0;
		boolean flag=false;
		for(int t=0; t<5; t++) {
			String[] str = br.readLine().split(" ");
			int[] a= new int[5];
			for(int i=0; i<5; i++) {
				 a[i] = Integer.parseInt(str[i]);
			}
			label : for(int i=0; i<5; i++) {
				for(int j=0; j<5; j++) {
					if(a[i]==pan[i][j]) {
						visited[i][j]=true;
						cnt++;
						break label;
					}
				}
			}
			for(int i=0; i<5; i++) {
				for(int j=0; j<5; j++) {
					System.out.print(visited[i][j]+" ");
				}
				System.out.println();
			}
			System.out.println();
			if(cnt>=5) {
				flag= detec(visited);
			}
			if(flag) {
				break;
			}
		}
		System.out.println(cnt);
		
	}
	static boolean detec(boolean[][] visited) {
		List<int[]> point = new ArrayList<>();
		int cnt=0;
		for(int i=0; i<5; i++) {
			if(visited[0][i]) {
				point.add(new int[] {0,i});
			}
		}
		for(int i=0; i<5; i++) {
			if(visited[i][0]) {
				point.add(new int[] {i,0});
			}
		}
		if(point.size()<=3) {
			return false;
		}
		int size = point.size();
		for(int i=0; i<size; i++) {
			boolean  flag = true;
			int x = point.get(i)[0];
			int y = point.get(i)[0];
			if((x==0 && y==0)||(x==0&&y==4)||(x==4 && y==0)) {
				for(int j=0; j<5; j++) {
					if(!visited[j][j]) {
						flag=false;
						break;
					}
				}
				if(!flag) {
					flag=true;
					for(int j=0; j<5; j++) {
						if(!visited[x][j]) {
							flag=false;
							break;
						}
					}
				}
				if(!flag) {
					flag=true;
					for(int j=0; j<5; j++) {
						if(!visited[j][y]) {
							flag = false;
							break;
						}
					}
				}
				if(flag) {
					cnt++;
				}
			}else if(x==0) {
				for(int j=0; j<5; j++) {
					if(!visited[j][y]) {
						flag=false;
						break;
					}
				}
				if(flag) {
					cnt++;
				}
			}else if(y==0) {
				for(int j=0; j<5; j++) {
					if(!visited[x][j]) {
						flag=false;
						break;
					}
				}
				if(flag) {
					cnt++;
				}
			}
		}
		if(cnt>=3) {
			return true;
		}
		return false;
	}

}
