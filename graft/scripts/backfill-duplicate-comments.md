# scripts/backfill-duplicate-comments.ts

- GitHubIssue · interface · L9-L17 — interface GitHubIssue
- GitHubComment · interface · L19-L24 — interface GitHubComment
- githubRequest · function · L26-L45 — async function githubRequest<T>(endpoint: string, token: string, method: string = 'GET', body?: any): Promise<T>
- triggerDedupeWorkflow · function · L47-L70 — async function triggerDedupeWorkflow( owner: string, repo: string, issueNumber: number, token: string, dryRun: boolean = true ): Promise<void>
- backfillDuplicateComments · function · L72-L208 — async function backfillDuplicateComments(): Promise<void>
