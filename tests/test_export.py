import tempfile
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
from instagram_analysis.export import account_names, comments, liked_post_owner, records


class ExportTests(unittest.TestCase):
    def write_export(self, body):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / 'export.html'
        path.write_text('<html><body><main>' + body + '</main></body></html>', encoding='utf-8')
        return path

    def test_new_owner_uses_username_not_field_heading_or_hashtag(self):
        record = BeautifulSoup('''<div><table><tr><td>URL</td><td><a href="https://instagram.com/p/123">post</a></td></tr></table>
        <div><h2>Eier</h2><table><tr><td>Navn</td><td>Display</td></tr>
        <tr><td>Brukernavn</td><td>real_user</td></tr></table></div>
        <div><h2>Emneknagger</h2><table><tr><td>Brukernavn</td><td>wrong</td></tr></table></div></div>''', 'html.parser')
        self.assertEqual(liked_post_owner(record), 'real_user')
        self.assertEqual(liked_post_owner(BeautifulSoup('<div><h2>Eier</h2></div>', 'html.parser')), None)
        self.assertEqual(liked_post_owner(BeautifulSoup('<div><h2>old_user</h2><a>👍</a></div>', 'html.parser')), 'old_user')

    def test_accounts_use_profile_fields_or_instagram_profile_links(self):
        path = self.write_export('''<div><table><tr><td>Brukernavn</td><td>user_one</td></tr></table>
        <a href="https://example.com/noise">noise</a></div>
        <div><a href="https://www.instagram.com/_u/user_two/">profile</a></div>
        <div><a href="https://instagram.com/user_three">user_three</a></div>''')
        self.assertEqual(account_names(path), {'user_one', 'user_two', 'user_three'})

    def test_comments_preserve_text_and_exclude_other_fields(self):
        path = self.write_export('''<div><table><tr><td>Comment<div><div>Comment &amp; hello</div></div></td></tr>
        <tr><td>Media Owner</td><td>someone</td></tr></table></div>
        <div><table><tr><td>Kommentar<div>Hei</div></td></tr></table></div>''')
        self.assertEqual(list(comments(path)), ['Comment & hello', 'Hei'])
        self.assertEqual(len(list(records(path))), 2)

    def test_records_span_read_chunks(self):
        path = self.write_export('<div><p>' + 'a' * 70000 + '</p></div><div><p>next</p></div>')
        self.assertEqual([r.p.get_text()[-4:] for r in records(path)], ['aaaa', 'next'])


if __name__ == '__main__':
    unittest.main()
