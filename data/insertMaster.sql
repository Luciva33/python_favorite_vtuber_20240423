-- VTuber事務所
INSERT INTO favorite_vtuber.m_offices (id, office_name) VALUES
(1, 'ホロライブ');

-- VTuberタグ
INSERT INTO favorite_vtuber.m_vtuber_tags (id, office_id, tag, tag_name) VALUES
(1, 1, 'gen-0', 'ホロライブ0期生'),
(2, 1, '1stgen', 'ホロライブ1期生'),
(3, 1, 'gen-2', 'ホロライブ2期生'),
(4, 1, 'gamers', 'ホロライブゲーマーズ'),
(5, 1, 'gen-3', 'ホロライブ3期生'),
(6, 1, 'gen-4', 'ホロライブ4期生'),
(7, 1, 'gen-5', 'ホロライブ5期生'),
(8, 1, 'holox', '秘密結社holoX'),
(9, 1, 'regloss', 'ReGLOSS'),
(10, 1, 'tag_office-staff', '事務所スタッフ');

-- VTuber情報
INSERT INTO favorite_vtuber.m_vtubers (id, office_id, name_ja, name_en, tag_id1, tag_id2, image_filename, thumbnail_filename, catch_text, introduction_video_url, youtube_url, twitter_url, recommended_video1, recommended_video2, recommended_video3) VALUES
