

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Round705 {
	static boolean check(int h,int min,int ch,int cm,HashMap<Integer, Integer>map) {
		String hr=ch+"";
		String mn=cm+"";
		if(hr.length()==1) {
			hr="0"+hr;
		}
		if(mn.length()==1) {
			mn="0"+mn;
		}
		StringBuffer chr=new StringBuffer(hr+mn);
		StringBuffer ans=new StringBuffer("");
		for(int i=0;i<chr.length();i++) {
		ans=ans.append(map.get(Character.getNumericValue(chr.charAt(i))));
		}
		ans.reverse();
		int first=Integer.parseInt(ans.substring(0, 2));
		int second=Integer.parseInt(ans.substring(2,4));
		if(first<h&&second<min) {
			return true;
		}
		return false;
	}
public static void main(String[] args) {
	Scanner o=new Scanner(System.in);
	int t=o.nextInt();
	while(t>0) {
		int h=o.nextInt();
		int m=o.nextInt();
		String st=o.next();
		int ch=Integer.parseInt(st.substring(0, 2));
		int cm=Integer.parseInt(st.substring(3,5));
			HashMap<Integer,Integer>map=new HashMap<>();
			map.put(0, 0);
			map.put(1, 1);
			map.put(2, 5);
			map.put(5, 2);
			map.put(8, 8);
			boolean ans=false;
			int hours=0;
			int minutes=0;
		for(int i=ch;i<h;i++) {
			for(int j=cm;j<m;j++) {
				String ckm=j+"";
				String chh=i+"";
				 if(ckm.length()==2) {
					
			 if(chh.length()==2) {
						if(map.containsKey(Character.getNumericValue(ckm.charAt(0)))&&map.containsKey(Character.getNumericValue(ckm.charAt(1)))&&map.containsKey(Character.getNumericValue(chh.charAt(0)))&&map.containsKey(Character.getNumericValue(chh.charAt(1)))) {
							if(check(h,m,i,j,map)) {
								
							ans=true;
							hours=i;
							minutes=j;
							break;
						}
						}
					}
					else {
						if(map.containsKey(Character.getNumericValue(ckm.charAt(0)))&&map.containsKey(Character.getNumericValue(ckm.charAt(1)))&&map.containsKey(Character.getNumericValue(chh.charAt(0)))) {
							if(check(h,m,i,j,map)) {
								
							ans=true;
							hours=i;
							minutes=j;
							break;
							}
						}
					}
				}
				else {
				
				 if(chh.length()==2) {
						if(map.containsKey(Character.getNumericValue(ckm.charAt(0)))&&map.containsKey(Character.getNumericValue(chh.charAt(0)))&&map.containsKey(Character.getNumericValue(chh.charAt(1)))) {
							if(check(h,m,i,j,map)) {
								
							ans=true;
							hours=i;
							minutes=j;
							break;
						}		
					}
					}
					else {
						if(map.containsKey(Character.getNumericValue(ckm.charAt(0)))&&map.containsKey(Character.getNumericValue(chh.charAt(0)))) {
							if(check(h,m,		i,j,map)) {
								
							ans=true;
							hours=i;
							minutes=j;
							break;	
					}
						}
				}
			}
			}
			if(ans) {
				break;
			}
			cm=0;
		}
		if(!ans) {
			System.out.println("00:00");	
		}
		else {
			String hrs=hours+"";
			if(hrs.length()==1)
				hrs=0+hrs;
			String mns=minutes+"";
			if(mns.length()==1)
				mns=0+mns;
			System.out.println(hrs+":"+mns);
		}
		t--;
	}
}
}
