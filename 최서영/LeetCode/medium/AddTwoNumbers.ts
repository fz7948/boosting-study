// https://leetcode.com/problems/add-two-numbers/

class ListNode {
  val: number
  next: ListNode | null

  constructor(val?:number, next?: ListNode | null) {
    this.val = (val === undefined ? 0: val)
    this.next = (next === undefined ? null : next)
  }
}

function getNumberFromList(list: ListNode): bigint {
  let numberStr = '';
  let runner: ListNode | null = list;

  while (runner) {
    numberStr = runner.val.toString() + numberStr;
    runner = runner.next;
  }

  return BigInt(numberStr);
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const n1 = getNumberFromList(l1);
  const n2 = getNumberFromList(l2);
  const sum = (n1 + n2).toString();

  let output: ListNode | null = null;

  for (let i = 0; i < sum.length; i++) {
    const digit = sum[i];
    output = new ListNode(Number(digit), output);
  }

  return output as ListNode;
};
