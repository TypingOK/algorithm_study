package baekjoon;

import java.util.*;

public class problem16935 {
	static int[][] arr;
	static int N;
	static int M;
	static int R;
	static int L;
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		R = sc.nextInt();
		
		arr = new int[N][M];
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				arr[i][j]=sc.nextInt();
			}
		}
		for(int i=0; i<R; i++) {
			L = sc.nextInt();
			switch (L) {
			case 1:
				one();
				break;
			case 2:
				two();
				break;
			case 3:
				int[][] copy = three();
				arr = copy;
				int temp = N;
				N = M;
				M = temp;
				two();
				break;
			case 4:
				int[][] copy2 = four();
				arr = copy2;
				int temp2 = N;
				N = M;
				M = temp2;
				one();
				two();
				break;
			case 5:
				five();
				break;
			case 6:
				six();
				break;
			}
		}
		print();
	}
	static void one() {
		for(int i=N-1; i>=N/2; i--) {
			int[] temp = arr[N-i-1];
			arr[N-i-1] = arr[i];
			arr[i]=temp;
//			System.out.println("i"+i+" : "+"i-N/2"+(N-i-1));
		}
	}
	static void two() {
		for(int j=M-1; j>=M/2; j--) {
			int[] temp = new int [N];
			for(int i=0; i<N; i++) {
				temp[i]=arr[i][M-j-1];
				arr[i][M-j-1] = arr[i][j];
				arr[i][j]=temp[i];
			}
		}
	}
	static int[][] three() {
		int[][] copy=new int [M][N];
		for(int i=0; i<M; i++) {
			int temp[] = new int[N];
			for(int j=0; j<N; j++) {
				temp[j]=arr[j][i];
			}
			for(int j=N-1;j>=0;j--) {
				copy[i][j]=temp[j];
			}
		}
		return copy;
		
	}
	static int[][] four() {
		int[][] copy=new int [M][N];
		for(int i=M-1; i>=0; i--) {
			int index=0;
			int temp[] = new int[N];
			for(int j=N-1; j>=0; j--) {
				temp[index]=arr[j][i];
				index++;
			}
			for(int j=N-1;j>=0;j--) {
				copy[i][j]=temp[j];
			}
		}
		return copy;
		
	}	
	static void five() {
		int[][] temp1=new int[N/2][M/2];
		int[][] temp2=new int[N/2][M/2];
		int[][] temp3=new int[N/2][M/2];
		int[][] temp4=new int[N/2][M/2];
		for(int i=0; i<N/2; i++) {
			for(int j=0; j<M/2; j++) {
				temp1[i][j]=arr[i][j];
			}
			for(int j=M/2; j<M; j++) {
				temp2[i][j-M/2]=arr[i][j];
			}
			for(int j=0; j<M/2; j++) {
				temp3[i][j]=arr[i+N/2][j];
			}
			for(int j=M/2; j<M; j++) {
				temp4[i][j-M/2]=arr[i+N/2][j];
			}
		}
//		int[][] copy = new int[N][M];
		for(int i=0; i<N/2; i++) {
			for(int j=0; j<M/2; j++) {
				arr[i][j] = temp3[i][j];
			}
			for(int j=M/2; j<M; j++) {
				arr[i][j]=temp1[i][j-M/2];
			}
			for(int j=0; j<M/2; j++) {
				arr[i+N/2][j]=temp4[i][j];
			}
			for(int j=M/2; j<M; j++) {
				arr[i+N/2][j]=temp2[i][j-M/2];
			}
		}
	}
	static void six() {
		int[][] temp1=new int[N/2][M/2];
		int[][] temp2=new int[N/2][M/2];
		int[][] temp3=new int[N/2][M/2];
		int[][] temp4=new int[N/2][M/2];
		for(int i=0; i<N/2; i++) {
			for(int j=0; j<M/2; j++) {
				temp1[i][j]=arr[i][j];
			}
			for(int j=M/2; j<M; j++) {
				temp2[i][j-M/2]=arr[i][j];
			}
			for(int j=0; j<M/2; j++) {
				temp3[i][j]=arr[i+N/2][j];
			}
			for(int j=M/2; j<M; j++) {
				temp4[i][j-M/2]=arr[i+N/2][j];
			}
		}
		for(int i=0; i<N/2; i++) {
			for(int j=0; j<M/2; j++) {
				arr[i][j] = temp2[i][j];
			}
			for(int j=M/2; j<M; j++) {
				arr[i][j]=temp4[i][j-M/2];
			}
			for(int j=0; j<M/2; j++) {
				arr[i+N/2][j]=temp1[i][j];
			}
			for(int j=M/2; j<M; j++) {
				arr[i+N/2][j]=temp3[i][j-M/2];
			}
		}
	}
	static void print() {
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		
	}
}
