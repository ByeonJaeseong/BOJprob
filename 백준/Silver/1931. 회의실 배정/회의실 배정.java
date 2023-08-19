import java.util.*;
import java.io.*;

public class Main
{
	public static void main (String[] args) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] sche = new int[n][2];
		int now = -1;	//현재시간
		for(int i = 0 ; i < n ; i++)
		{
			int start = sc.nextInt();
			int end = sc.nextInt();
			
			sche[i][0] = start;
			sche[i][1] = end;
		}
		
		Arrays.sort(sche, new Comparator<int[]>()
		//정렬 완료
		{
			public int compare(int[]o1 , int[]o2)
			{
				if(o1[1] == o2[1])
				{
					//끝시간 동일 시작시간 기준으로 정렬
					return o1[0] - o2[0];
				}
				else
				{   //아닐 경우 그냥 끝시간으로 정렬
					return o1[1] - o2[1];
				}
			}
		});
        int cnt = 1;
        now = sche[0][1];
        for(int i = 1 ; i < n ; i++)
        {
            if(now <= sche[i][0])
            {
                now = sche[i][1];
                cnt++;
            }
        }
		System.out.println(cnt);
	}
	
}