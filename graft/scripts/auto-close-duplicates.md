# scripts/auto-close-duplicates.ts

- GitHubIssue · interface · L9-L14 — interface GitHubIssue
- GitHubComment · interface · L16-L21 — interface GitHubComment
- GitHubReaction · interface · L23-L26 — interface GitHubReaction
- githubRequest · function · L28-L47 — async function githubRequest<T>(endpoint: string, token: string, method: string = 'GET', body?: any): Promise<T>
- extractDuplicateIssueNumber · function · L49-L63 — function extractDuplicateIssueNumber(commentBody: string): number | null
- closeIssueAsDuplicate · function · L66-L97 — async function closeIssueAsDuplicate( owner: string, repo: string, issueNumber: number, duplicateOfNumber: number, token: string ): Promise<void>
- autoCloseDuplicates · function · L99-L272 — async function autoCloseDuplicates(): Promise<void>
