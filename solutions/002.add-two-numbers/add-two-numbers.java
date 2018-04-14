/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode head = new ListNode(0);
        ListNode list = head;
        boolean add = false;
        int divide = -1;
        int val = -1;


        while(l1 != null && l2 != null){
                
            if(add == true){
                val = 1;
                add = false;
            }else{
                val = 0;
            }
                
            int value = (l1.val + l2.val + val) % 10;
            divide = (l1.val + l2.val + val) / 10;

            
            ListNode node = new ListNode(value);
            list.next = node;
            list = list.next;
            l1 = l1.next;
            l2 = l2.next;
            

            if(divide == 1){
                add = true;
            }
            
        }
        
        ListNode l = null;

        if(l1 != null){
           
           l = l1;
           
        }else if (l2 != null){
            l = l2;
        }
        
        if(l != null){
            
            while(l != null){
            
                if(add == true){
                    val = 1;
                    add = false;
                }else{
                    val = 0;
                }
                
                int value = (l.val + val) % 10;
                divide = (l.val + val) / 10;
                list.next = new ListNode(value);
                list = list.next;
                l = l.next;
                
                if(divide == 1){
                    add = true;
                }
                
            }
            
        }
            
        if(add == true){
            list.next = new ListNode(1);
        }
        
        return head.next;
    }
}