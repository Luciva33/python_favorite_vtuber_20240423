-- drop DB
drop database if exists favorite_vtuber;

-- create DB
CREATE DATABASE favorite_vtuber DEFAULT CHARACTER SET utf8;

-- VTuber事務所
CREATE TABLE favorite_vtuber.m_offices (
    id INT PRIMARY KEY AUTO_INCREMENT,
    office_name varchar(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- VTuberタグ情報
CREATE TABLE favorite_vtuber.m_vtuber_tags (
    id INT PRIMARY KEY AUTO_INCREMENT,
    office_id int NOT NULL,
    tag varchar(30) NOT NULL,
    tag_name varchar(30) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (office_id) REFERENCES m_offices(id)
);

-- VTuber情報
CREATE TABLE favorite_vtuber.m_vtubers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    office_id int NOT NULL,
    name_ja varchar(30) NOT NULL,
    name_en varchar(30),
    tag_id1 int NOT NULL,
    tag_id2 int,
    image_filename varchar(20) NOT NULL,
    thumbnail_filename varchar(20) NOT NULL,
    catch_text text,
    introduction_video_url varchar(30),
    youtube_url varchar(30),
    twitter_url varchar(30),
    recommended_video1 varchar(30),
    recommended_video2 varchar(30),
    recommended_video3 varchar(30),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (office_id) REFERENCES m_offices(id),
    FOREIGN KEY (tag_id1) REFERENCES m_vtuber_tags(id),
    FOREIGN KEY (tag_id2) REFERENCES m_vtuber_tags(id)
);

-- VTuberプロフィール情報
CREATE TABLE favorite_vtuber.m_vtubers_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vtuber_id int NOT NULL,
    title varchar(50),
    content text not null,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vtuber_id) REFERENCES m_vtubers(id)
);

-- お気に入り動画タグ情報
CREATE TABLE favorite_vtuber.m_favorite_video_tags (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tag varchar(30) NOT NULL,
    tag_name varchar(30) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ユーザ情報
CREATE TABLE favorite_vtuber.m_users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    password varchar(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- お気に入りVTuber情報
CREATE TABLE favorite_vtuber.t_favorite_vtubers (
    user_id int NOT NULL,
    vtuber_id int NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES m_users(id),
    FOREIGN KEY (vtuber_id) REFERENCES m_vtubers(id),
    PRIMARY KEY (user_id, vtuber_id)
);

-- お気に入り動画情報
CREATE TABLE favorite_vtuber.t_favorite_videos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id int NOT NULL,
    vtuber_id int NOT NULL,
    video_url varchar(50) NOT NULL,
    tag_id1 int,
    tag_id2 int,
    tag_id3 int,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES m_users(id),
    FOREIGN KEY (vtuber_id) REFERENCES m_vtubers(id),
    FOREIGN KEY (tag_id1) REFERENCES m_favorite_video_tags(id),
    FOREIGN KEY (tag_id2) REFERENCES m_favorite_video_tags(id),
    FOREIGN KEY (tag_id3) REFERENCES m_favorite_video_tags(id)
);