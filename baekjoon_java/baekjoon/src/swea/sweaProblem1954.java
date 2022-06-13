package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class sweaProblem1954 {
	static int[] dx = {0,-1,0,1};
	static int[] dy = {1,0,-1,0};
	public static void main(String[] args) throws IOException{
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=TC; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[][] arr = new int[n][n];
			int num =1;
			int x=0;
			int y=0;
			int i=0;
			arr[0][0]=1;
			while(num<(n*n)) {
				int nx =x+dx[i];
				int ny = y+dy[i];
				
				if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]==0) {
					arr[nx][ny]=++num;
					x=nx;
					y=ny;
				}else {
					i++;
					if(i%4==0) {
						i=0;
					}
				}
				
			}
			System.out.println("#"+tc);
			for(int k=0; k<n;k++) {
				for(int j=0; j<n; j++) {
					System.out.print(arr[k][j]+" ");
				}
				System.out.println();
			}
		}
		
	}

}
