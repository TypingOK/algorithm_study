package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class problem2239 {
	
	static ArrayList<int[]> list = new ArrayList<>();
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] map = new int[9][9];
		char[] str;
		for(int i=0; i<9; i++) {
			str = br.readLine().toCharArray();
			for(int j=0; j<9; j++) {
				map[i][j] = (int)str[j]-'0';
				if(map[i][j] == 0 ) {
					list.add(new int[] {i,j});
				}
			}
		}
		comb(0,map);
	}
	public static void comb(int index,int[][] map) {
		if(index == list.size()) {
			if(asd(map) == 0) {
				for(int i=0; i<9; i++) {
					for(int j=0; j<9; j++) {
						System.out.print(map[i][j]);
					}
					System.out.println();
				}
				System.exit(0);
			}
		return ;
		}
		
		int newMap[][] = new int[9][9];
		
		int number[] = new int[10];
		int temp[] = list.get(index);
		
		copy(map,newMap);
		leftRight(newMap,temp[0],temp[1],number);
		three(newMap,temp[0],temp[1],number);
		for(int i=1; i<=9; i++) {
			if(number[i]==2) {
				newMap[temp[0]][temp[1]] = i;
				comb(index+1,newMap);
			}
		}
		
		
	}
	public static int[][] copy (int[][] map, int [][] newMap){
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				newMap[i][j] = map[i][j];
			}
		}
		return newMap;
	}
	public static int asd(int map[][]) {
		int sum =0;
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(map[i][j] == 0) {
					sum++;
				}
			}
		}
		return sum;
	}
	public static void leftRight(int map[][],int x,int y,int number[]) {
		label: for(int j=1; j<=9; j++) {
			for(int i=0; i<9; i++) {
				if(map[x][i]==j) {
					continue label;
				}
			}
			for(int i=0; i<9; i++) {
				if(map[i][y]==j) {
					continue label;
				}
			}
			number[j]++;
		}
	}
	public static void three(int map[][], int x, int y,int number[]) {
		if(x%3==0) {
			if(y%3==0) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x; i<=x+2; i++) {
						for(int j=y; j<y+2; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==1) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x; i<=x+2; i++) {
						for(int j=y-1; j<=y+1; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==2) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x; i<=x+2; i++) {
						for(int j=y-2; j<=y; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
				
			}
		} else if(x%3==1) {
			if(y%3==0) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-1; i<=x+1; i++) {
						for(int j=y; j<=y+2; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==1) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-1; i<=x+1; i++) {
						for(int j=y-1; j<=y+1; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==2) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-1; i<=x+1; i++) {
						for(int j=y-2; j<=y; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
				
			}
		} else if (x%3==2) {
			if(y%3==0) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-2; i<=x; i++) {
						for(int j=y; j<=y+2; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==1) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-2; i<=x; i++) {
						for(int j=y-1; j<=y+1; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}else if(y%3==2) {
				label: for(int k=1; k<=9; k++) {
					for(int i=x-2; i<=x; i++) {
						for(int j=y-2; j<=y; j++) {
							if(map[i][j]==k) {
								continue label;
							}
						}
					}
					number[k]++;
				}
			}
		}
	}
	
}
