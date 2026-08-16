import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeSet;

import javax.print.attribute.standard.MediaSize.Other;
import javax.xml.bind.ParseConversionEvent;

public class Main {
	
	public static final int MAX_MUSIC = 50;
	public static final int MAX = 8;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
	
		final int n = sc.nextInt();
		final int m = sc.nextInt();
		
		int[][][] DP = new int[n + 1][m + 1][MAX + 1];
		
		for(int i = 0; i <= n; i++){
			for(int j = 0; j <= m; j++){
				Arrays.fill(DP[i][j], Integer.MIN_VALUE);
			}
		}
		
		int[][] sat = new int[n][3];
		for(int i = 0; i < n; i++){
			for(int j = 0; j < 3; j++){
				sat[i][j] = sc.nextInt();
			}
		}
		
		DP[0][m][0] = 0;
		for(int music = 0; music < n; music++){
			for(int level2 = 0; level2 <= m; level2++){
				for(int level1 = 0; level1 <= MAX; level1++){
					if(DP[music][level2][level1] == Integer.MIN_VALUE){
						continue;
					}
					
					final int limit = Math.min(MAX, level2);
					for(int burn = 0; burn <= limit; burn++){
						DP[music + 1][level2 - burn][burn] = Math.max(DP[music + 1][level2 - burn][burn], DP[music][level2][level1] + sat[music][2]);
					}
					
					final int limit_2 = Math.min(level2, MAX);
					final int limit_1 = Math.min(level1, MAX);
					
					for(int use_2 = 0; use_2 <= limit_2; use_2++){
						for(int use_1 = 0; use_1 <= limit_1; use_1++){
							if(use_2 == 0 && use_1 == 0){
								continue;
							}else if(use_1 + use_2 > MAX){
								break;
							}
							
							final int benefit = sat[music][0] * use_2 + sat[music][1] * use_1;
							
							final int limit_burn = Math.min(level2 - use_2, MAX - use_2);
							for(int burn = 0; burn <= limit_burn; burn++){
								DP[music + 1][level2 - use_2 - burn][use_2 + burn] = Math.max(DP[music + 1][level2 - use_2 - burn][use_2 + burn], DP[music][level2][level1] + benefit);
							}
						}
					}
				}
			}
		}
		
		int max = Integer.MIN_VALUE;
		for(int level2 = 0; level2 <= m; level2++){
			for(int level1 = 0; level1 <= MAX; level1++){
				//System.out.println(DP[n][level2][level1]);
				max = Math.max(max, DP[n][level2][level1]);
			}
		}
		
		System.out.println(max);
	}

}