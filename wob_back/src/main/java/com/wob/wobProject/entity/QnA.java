package com.wob.wobProject.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "qna")
@Getter
@Setter
@ToString
@NoArgsConstructor
public class QnA {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "qna_id")
    private Long Id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(nullable = false)
    private String chat;

    private LocalDateTime regDate;

    @PrePersist
    public void prePersist() {
        regDate = LocalDateTime.now();
    }

    private Boolean active;
    private String qnaUuid;


}